from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from app.services.age import calculate_age
from app.services.battery import get_battery_status
from app.services.currency import convert_currency
from app.services.discover_mobile_operator import get_operator
from app.services.download_file import download_file
from app.services.json_generator import generate_json
from app.services.password import generate_password
from app.services.pc_info import get_pc_info
from app.services.pdf_generator import generate_pdf
from app.services.qrcode_generator import generate_qrcode
from app.services.qrcode_reader import read_qrcode
from app.services.speedtest_service import run_speedtest


def success(data):
    return Response({"success": True, "data": data})


def error(e):
    return Response(
        {"success": False, "error": str(e)},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


@api_view(["GET"])
def password_view(request):
    try:
        return success({"password": generate_password()})
    except Exception as e:
        return error(e)


@api_view(["GET"])
def age_view(request):
    try:
        birthdate = request.GET.get("birthdate")
        return success({"age": calculate_age(birthdate)})
    except Exception as e:
        return error(e)


@api_view(["GET"])
def battery_view(request):
    try:
        return success(get_battery_status())
    except Exception as e:
        return error(e)


@api_view(["GET"])
def currency_view(request):
    try:
        amount = float(request.GET.get("amount", 1))
        from_currency = request.GET.get("from", "USD")
        to_currency = request.GET.get("to", "BRL")

        return success({"result": convert_currency(amount, from_currency, to_currency)})
    except Exception as e:
        return error(e)


@api_view(["GET"])
def operator_view(request):
    try:
        phone = request.GET.get("phone")
        return success({"operator": get_operator(phone)})
    except Exception as e:
        return error(e)


@api_view(["GET"])
def download_view(request):
    try:
        url = request.GET.get("url")
        return success({"file": download_file(url)})
    except Exception as e:
        return error(e)


@api_view(["GET"])
def json_view(request):
    try:
        return success(generate_json())
    except Exception as e:
        return error(e)


@api_view(["GET"])
def pc_info_view(request):
    try:
        return success(get_pc_info())
    except Exception as e:
        return error(e)


@api_view(["GET"])
def pdf_view(request):
    try:
        content = request.GET.get("content", "Hello World")
        return success({"pdf": generate_pdf(content)})
    except Exception as e:
        return error(e)


@api_view(["GET"])
def qrcode_generate_view(request):
    try:
        data = request.GET.get("data", "test")
        return success({"qrcode": generate_qrcode(data)})
    except Exception as e:
        return error(e)


@api_view(["GET"])
def qrcode_read_view(request):
    try:
        path = request.GET.get("path")
        return success({"content": read_qrcode(path)})
    except Exception as e:
        return error(e)


@api_view(["GET"])
def speedtest_view(request):
    try:
        return success(run_speedtest())
    except Exception as e:
        return error(e)
