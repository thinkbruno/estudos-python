document.addEventListener("DOMContentLoaded", () => {

    document.getElementById("btnPassword").addEventListener("click", async () => {
        const length = document.getElementById("length").value;
        const response = await fetch(`/utils/password?length=${length}`);
        const data = await response.json();
        document.getElementById("passwordResult").innerText = data.password;
    });

    document.getElementById("btnAge").addEventListener("click", async () => {
        const birth = document.getElementById("birthdate").value;
        const response = await fetch(`/age/calculate?birth_date=${birth}`);
        const data = await response.json();

        document.getElementById("ageResult").innerText =
            data.detail
                ? data.detail
                : `${data.years} ano(s), ${data.months} mês(es), ${data.days} dia(s)`;
    });

    document.getElementById("btnBattery").addEventListener("click", async () => {
        const response = await fetch(`/battery/`);
        const data = await response.json();

        document.getElementById("batteryResult").innerText =
            data.detail ? data.detail : `Bateria: ${data.battery_percent}%`;
    });

    document.getElementById("btnCurrency").addEventListener("click", async () => {
        const amount = document.getElementById("usdAmount").value;
        if (!amount || amount <= 0) {
            document.getElementById("currencyResult").innerText = "Informe um valor válido.";
            return;
        }

        const response = await fetch(`/currency/usd-to-brl?amount=${amount}`);
        const data = await response.json();

        document.getElementById("currencyResult").innerText =
            data.detail ? data.detail : `USD ${data.usd} = R$ ${data.brl}`;
    });

    document.getElementById("btnJson").addEventListener("click", () => {
        window.location.href = "/json-generator";
    });

    document.getElementById("btnOperator").addEventListener("click", async () => {
        const number = document.getElementById("phone").value;
        const response = await fetch(`/discover-operator?number=${number}`);
        const data = await response.json();

        document.getElementById("operatorResult").innerText =
            response.status === 200
                ? `Operadora: ${data.operadora} | Estado: ${data.estado}`
                : data.detail;
    });

    document.getElementById("btnDownloadText").addEventListener("click", () => {
        const url = document.getElementById("urlInput").value;
        if (!url) return alert("Digite uma URL válida");

        window.location.href = `/download-text?url=${encodeURIComponent(url)}`;
    });

    document.getElementById("btnPdf").addEventListener("click", () => {
        window.location.href = "/generate-pdf";
    });

    document.getElementById("btnSpeedtest").addEventListener("click", async () => {
        const result = document.getElementById("speedResult");
        result.innerText = "Executando...";

        const response = await fetch("/speedtest");
        const data = await response.json();

        result.innerText =
            response.status === 200
                ? `Download: ${data.download_mbps} Mbps | Upload: ${data.upload_mbps} Mbps`
                : data.detail;
    });

    document.getElementById("btnQrGenerate").addEventListener("click", () => {
        const url = document.getElementById("qrUrl").value;
        if (!url) return alert("Digite uma URL válida");

        window.open(`/generate-qrcode?url=${encodeURIComponent(url)}`, "_blank");
    });

    document.getElementById("btnQrRead").addEventListener("click", async () => {
        const file = document.getElementById("qrFile").files[0];
        if (!file) return alert("Selecione uma imagem");

        const formData = new FormData();
        formData.append("file", file);

        const response = await fetch("/read-qrcode", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        const result = document.getElementById("qrResult");

        result.innerText =
            response.status === 200 ? data.content : data.detail;

        if (response.status === 200 && data.content.startsWith("http")) {
            window.open(data.content, "_blank");
        }
    });

    document.getElementById("btnPcInfo").addEventListener("click", async () => {
        const response = await fetch("/pc-info");
        const data = await response.json();

        document.getElementById("pcInfoResult").innerText =
            JSON.stringify(data, null, 2);
    });

});
