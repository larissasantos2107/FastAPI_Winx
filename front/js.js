async function puxando_api() {
    const response = await fetch("http://localhost:8001/api/v1/winx/");
    const data = await response.json();
    return data;
}

async function mostra_info() {
    const winx = await puxando_api();
    const conteiner = document.getElementById("winx-conteiner");

    winx.forEach(winx => {
        const winxDiv = document.createElement("div");
        winxDiv.classList.add("winx");
        winxDiv.innerHTML = `
            <h2>${winx.nome}</h2>
            <img src="${winx.foto}" alt="Foto da ${winx.nome}">
            <p><strong>Poder:</strong> ${winx.poder}</p>
            <p><strong>Mundo:</strong> ${winx.mundo}</p>
            <p><strong>Faz parte do Clube Winx?</strong> ${winx.pertenceWinx}</p>
        `;
        conteiner.appendChild(winxDiv);
    });
}

mostra_info();
