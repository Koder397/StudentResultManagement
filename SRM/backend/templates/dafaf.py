class CityList(ListView):
    model = City

    template_name = "backend/city/list.html"


class CityNew(CreateView):
    model = City

    template_name = "backend/city/create.html"

    fields = "__all__"

    success_url = "/backend/city"


class CityUpdate(UpdateView):
    model = City

    template_name = "backend/city/update.html"

    fields = "__all__"

    success_url = "/backend/city"


class CityDelete(DeleteView):
    model = City

    template_name = "backend/city/delete.html"

    success_url = "/backend/city"