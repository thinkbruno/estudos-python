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

        const button = document.getElementById("btnCurrency");
        const result = document.getElementById("currencyResult");
        const amount = document.getElementById("usdAmount").value;

        if (!amount) {
            result.innerHTML = "Informe um valor.";
            return;
        }

        button.disabled = true;
        button.innerHTML = 'Convertendo <span class="spinner"></span>';
        result.innerHTML = '<span class="loading-text">Buscando cotação...</span>';

        try {
            const response = await fetch(`/currency/usd-to-brl?amount=${amount}`);
            const data = await response.json();
            result.innerHTML = `R$ ${data.brl}`;

        } catch (error) {
            result.innerHTML = "Erro ao converter moeda.";
        } finally {
            button.disabled = false;
            button.innerHTML = "Converter";
        }

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

        const button = document.getElementById("btnSpeedtest");
        const result = document.getElementById("speedResult");

        // Estado de loading
        button.disabled = true;
        button.innerHTML = 'Executando <span class="spinner"></span>';
        result.innerHTML = '<span class="loading-text">Testando velocidade...</span>';

        try {
            const response = await fetch("/speedtest");
            const data = await response.json();
            result.innerHTML = `
                Download: ${data.download_mbps} Mbps<br>
                Upload: ${data.upload_mbps} Mbps<br>
            `;

        } catch (error) {
            result.innerHTML = "Erro ao executar speedtest.";
        } finally {
            button.disabled = false;
            button.innerHTML = "Executar";
        }

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

        const modal = document.getElementById("pcModal");
        const content = document.getElementById("pcModalContent");

        content.innerHTML = "Carregando...";

        modal.style.display = "block";

        try {
            const response = await fetch("/pc-info");
            const data = await response.json();

            content.innerHTML = `
                <ul class="pc-list">
                    <li><span>Sistema:</span> ${data.sistema_operacional}</li>
                    <li><span>Versão:</span> ${data.versao_sistema}</li>
                    <li><span>Arquitetura:</span> ${data.arquitetura}</li>
                    <li><span>Processador:</span> ${data.processador || "Não disponível"}</li>
                    <li><span>Núcleos físicos:</span> ${data.nucleos_cpu}</li>
                    <li><span>Núcleos lógicos:</span> ${data.nucleos_logicos}</li>
                    <li><span>Memória total:</span> ${data.memoria_total_gb} GB</li>
                    <li><span>Uso de memória:</span> ${data.memoria_usada_percentual}%</li>
                </ul>
            `;

        } catch (error) {
            content.innerHTML = "Erro ao carregar informações.";
        }

    });

    // Fechar modal
    document.getElementById("closePcModal").addEventListener("click", () => {
        document.getElementById("pcModal").style.display = "none";
    });

    // Fechar clicando fora
    window.addEventListener("click", (event) => {
        const modal = document.getElementById("pcModal");
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

});
