from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import update_avatar
from api.views import (
    IngredientViewSet,
    RecipeViewSet,
    TagViewSet,
    UserSubscribeView,
    UserSubscriptionsViewSet,
    RecipeShortLinkView,
    UserMeView
)

router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('users/me/', UserMeView.as_view(), name='user-me'),
    path('users/me/avatar/', update_avatar),
    path('users/subscriptions/',
         UserSubscriptionsViewSet.as_view({'get': 'list'})),
    path('users/<int:user_id>/subscribe/', UserSubscribeView.as_view()),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('recipes/<int:pk>/get-link/', RecipeShortLinkView.as_view(),
         name='get_recipe_short_link'),
]
