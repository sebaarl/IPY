from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views import generic
from productos.models import Producto
from cart.models import OrderItem, Address, Payment, Order
from .forms import AddToCartForm, AddressForm
from .utils import get_or_set_order_session
from django.shortcuts import get_object_or_404, reverse, redirect


# Create your views here.
class ProductListView(generic.ListView):
    template_name = 'cart/product_list.html'
    queryset = Producto.objects.all()

class ProductDetailView(generic.FormView):
    template_name = 'cart/product_detail.html'
    form_class = AddToCartForm

    def get_object(self):
        return get_object_or_404(Producto, slug=self.kwargs["slug"])

    def get_success_url(self):
        return reverse("home")

    def get_form_kwargs(self):
        kwargs = super(ProductDetailView, self).get_form_kwargs()
        kwargs["product_id"] = self.get_object().id
        return kwargs

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        product = self.get_object()

        item_filter = order.items.filter(product=product)

        if item_filter.exists():
            item = item_filter.first()
            item.quantity += int(form.cleaned_data['quantity'])
            item.save()

        else:
            new_item = form.save(commit=False)
            new_item.product = product
            new_item.order = order
            new_item.save()
        
        return super(ProductDetailView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = self.get_object()

        return context

class CartView(generic.TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        return context

class IncreaseQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.quantity += 1
        order_item.save()
        return redirect("cart:summary")


class DecreaseQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])

        if order_item.quantity <= 1:
            order_item.delete()
        else:
            order_item.quantity -= 1
            order_item.save()
        return redirect("cart:summary")

class RemoveFromCartView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.delete()
        return redirect("cart:summary")
