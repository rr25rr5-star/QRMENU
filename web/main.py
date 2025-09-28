from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uuid, os, asyncio
from bot.config import ORDER_CHANNEL
from run import bot
from bot.config import BOT

app = FastAPI()
os.makedirs("web/static", exist_ok=True)
app.mount("/static", StaticFiles(directory="web/static"), name="static")

# in-memory DB
items = {}
carts = {}

@app.get("/", response_class=HTMLResponse)
def menu():
    return """
<h1>Menu</h1>
<button onclick="add(1,'Burger',28000)">Burger 28 000</button>
<button onclick="add(2,'Cola',12000)">Cola 12 000</button>
<hr>
<button onclick="checkout()">📤 Buyurtma berish</button>
<div id="cart"></div>
<script>
let cart=JSON.parse(localStorage.getItem('cart')||'{}');
function add(id,name,price){
    cart[id]={name,price,qty:(cart[id]?.qty||0)+1};
    localStorage.setItem('cart',JSON.stringify(cart));
    render();
}
function render(){
    let h='',t=0;
    for(let i in cart){let c=cart[i];h+=`${c.name} × ${c.qty}<br>`;t+=c.price*c.qty;}
    document.getElementById('cart').innerHTML=h+`<hr>Jami: ${t}`;
}
render();
async function checkout(){
    if(!Object.keys(cart).length){alert("Savat bo'sh");return;}
    const username = prompt("Username kiriting (@siz):");
    const stol = prompt("Stol raqami:");
    await fetch('/checkout',{
        method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({username,stol,items:Object.values(cart)})
    });
    alert("Buyurtma yuborildi!");
    localStorage.removeItem('cart');
    location.reload();
}
</script>
"""

@app.post("/checkout")
async def checkout(data: dict):
    username, stol, items = data["username"], data["stol"], data["items"]
    total = sum(i["qty"]*i["price"] for i in items)
    text = f"<b>Yangi buyurtma</b>\n<b>Stol:</b> {stol}\n<b>Mijoz:</b> @{username}\n\n"
    for i in items:
        text += f"• {i['name']} × {i['qty']} = {i['qty']*i['price']} so‘m\n"
    text += f"\n<b>Jami:</b> {total:,} so‘m"
    await bot.send_message(f"@{ORDER_CHANNEL}", text, parse_mode="HTML")
    return JSONResponse({"ok": True})