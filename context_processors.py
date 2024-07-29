from mainapp.models import AddtoCart,Order


def CartCount(request):
    if request.user.is_authenticated:
        count=AddtoCart.objects.filter(user=request.user).exclude(status='order-placed').count()
        return {'count':count}
    else:
        return{'count':0}
def Order_count(request):
    if request.user.is_authenticated:
        data=Order.objects.filter(user=request.user).count
        return{'ordercount':data}
    else:
        return{'ordercount':0}