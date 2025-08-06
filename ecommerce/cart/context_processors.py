from .models import Cart

def cart_processor(request):
    if not request.session.session_key:
        request.session.create()

    cart, created = Cart.objects.get_or_create(
        session_key=request.session.session_key
    )

    return {
        'cart_total_items': cart.total_items,
        'cart_subtotal': cart.subtotal
    }


# Контекстний процесор працює завжди на фоні сайту, сюди ми поміщаємо ті речі які ми хочемо, щоб відображались постійно
# Іншими словами це контекст який завжди буде передавтись в шаблон ( корисно коли хочемо, щоб щось постійно
# відображалось , при переході на будь-яку сторінку )