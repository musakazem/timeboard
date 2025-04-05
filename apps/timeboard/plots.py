import matplotlib.pyplot as plt
from apps.timeboard.models import ProductivityDaily
from datetime import datetime, timedelta

def plot_productivity_chart(days_lower_limit):
    date_range = datetime.now() - timedelta(days=days_lower_limit)
    productivity_data = ProductivityDaily.objects.filter(date__gte=date_range).order_by('date')

    dates = [entry.date for entry in productivity_data]
    scores = [entry.score for entry in productivity_data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, scores, marker='o', linestyle='-', color='b', label='Productivity Score')

    plt.fill_between(dates, scores, color='blue', alpha=0.2)

    plt.xlabel('Date')
    plt.ylabel('Score')
    plt.title('Productivity Scores Over Time')
    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
