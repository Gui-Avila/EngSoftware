async function api(path) {
    const res = await fetch(path);
    return res.json();
}

function formatCurrency(value) {
    return "R$ " + value.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

function formatDate(iso) {
    const [y, m, d] = iso.split("-");
    return d + "/" + m + "/" + y;
}

function esc(str) {
    const el = document.createElement("span");
    el.textContent = str;
    return el.innerHTML;
}

function toast(msg, type = "success") {
    let container = document.querySelector(".toast-container");
    if (!container) {
        container = document.createElement("div");
        container.className = "toast-container";
        document.body.appendChild(container);
    }
    const el = document.createElement("div");
    el.className = "toast toast-" + type;
    el.textContent = msg;
    container.appendChild(el);
    setTimeout(() => el.remove(), 3000);
}
