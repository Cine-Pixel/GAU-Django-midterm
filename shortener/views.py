from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse

from http import HTTPStatus

from .models import Surl
from .forms import UrlForm
from .utils import make_short_url


class ShortenView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request: HttpRequest):
        form = UrlForm()
        short = request.GET.get("short", None)

        context = {
            "form": form,
            "home_link": "active",
            "short_url": f"{request.get_host()}/{short}" if short else None
            # "short_url": f"sm.rl/{short}" if short else None
        }

        return render(request, 'shortener/index.html', context)

    def post(self, request: HttpRequest):
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            short = make_short_url()

            while Surl.objects.filter(short=short).exists():
                short = make_short_url()

            surl = Surl(url=url, short=short, owner=request.user)
            surl.save()

            return redirect(reverse("shortener:index")+"?short="+short)


class RedirectView(View):
    def get(self, request: HttpRequest, short: str, *args, **kwargs):
        surl = Surl.objects.filter(short=short).first()
        if surl:
            surl.visit_count += 1
            surl.save()
            return redirect(surl.url)

        return render(request, '404.html', {})


class DashboardView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request: HttpRequest):
        surls = Surl.objects.filter(owner=request.user).order_by('id')
        paginator = Paginator(surls, 5)

        page_number = request.GET.get('page', 1)
        surls_on_page = paginator.get_page(page_number)

        context = {
            "surls": surls_on_page,
            "dashboard_link": "active"
        }
        return render(request, "shortener/dashboard.html", context)


class DeleteView(LoginRequiredMixin, View):
    login_url = "/login/"

    def post(self, request: HttpRequest):
        id = request.POST.get('smrl_id')
        surl = Surl.objects.filter(id=id).first()
        if surl:
            if surl.owner == request.user:
                surl.delete()
                return JsonResponse({"message": "success"}, status=HTTPStatus.OK)
            return JsonResponse({"message": "Permision denied"}, status=HTTPStatus.METHOD_NOT_ALLOWED)
        return JsonResponse({"message": "Smrl not found"}, status=HTTPStatus.NOT_FOUND)

