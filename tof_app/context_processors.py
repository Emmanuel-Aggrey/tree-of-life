from .models import Article

def articles(request):
    articles = Article.objects.order_by('-date_updated')
    return {'allarticles':articles}

