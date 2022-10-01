from django.db.models import Sum
from django.utils import timezone
from django.views.generic import ListView
from .models import SheetData


# Представление для отображения данных таблицы
class SheetsDataListView(ListView):
    model = SheetData
    template_name = 'main_app/sheet_data.html'
    context_object_name = 'sheet_data'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SheetsDataListView, self).get_context_data(**kwargs)
        # Добавление в контекст суммы цены всех заказов в долларах
        context['total'] = self.object_list.aggregate(total=Sum('price_dol'))['total']
        # Добавление в контекст данных для построение графика
        context['chart_data'] = [int(item.price_dol) for item in self.object_list]
        context['chart_labels'] = [str(item.shipment_date) for item in self.object_list]
        # Добавление в контекст показателя текущего времени
        context['cur_time'] = timezone.localtime(timezone.now())
        return context
