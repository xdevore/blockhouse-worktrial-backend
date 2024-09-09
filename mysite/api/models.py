from django.db import models

class CandlestickData(models.Model):
    data = models.JSONField(default={"data":[{"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
                                             {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40}]})
    
class LineChartData(models.Model):
    data = models.JSONField(default={"labels":["Jan", "Feb", "Mar", "Apr"], "data":[10, 20, 30, 40]})
    
class BarChartData(models.Model):
    data = models.JSONField(default={"labels":["Product A", "Product B", "Product C"], "data":[100, 150, 200]})
    
class PieChartData(models.Model):
    data = models.JSONField(default={"labels":["Red", "Blue", "Yellow"], "data":[300, 50, 100]})