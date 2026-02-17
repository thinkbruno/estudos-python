import speedtest


def run_speedtest() -> dict:
    try:
        st = speedtest.Speedtest()

        download = st.download()
        upload = st.upload()

        download_mbps = round(download / 1e6, 2)
        upload_mbps = round(upload / 1e6, 2)

        return {"download_mbps": download_mbps, "upload_mbps": upload_mbps}

    except Exception:
        raise ValueError("Erro ao executar speedtest")
