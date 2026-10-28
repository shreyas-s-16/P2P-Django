from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='dashboard'),
    path('links', views.links_collection_api, name='links_collection'),
    path('links/', views.links_collection_api, name='links_collection_slash'),
    path('api/links', views.links_collection_api, name='api_links_collection'),
    path('api/links/', views.links_collection_api, name='api_links_collection_slash'),

    path('links/stats', views.stats_api, name='stats_api'),
    path('links/stats/', views.stats_api, name='stats_api_slash'),
    path('api/links/stats', views.stats_api, name='api_stats_api'),
    path('api/links/stats/', views.stats_api, name='api_stats_api_slash'),

    path('links/<int:link_id>/restore', views.restore_link_api, name='restore_link_api'),
    path('links/<int:link_id>/restore/', views.restore_link_api, name='restore_link_api_slash'),
    path('api/links/<int:link_id>/restore', views.restore_link_api, name='api_restore_link_api'),

    path('links/<str:identifier>/qr', views.qr_code_api, name='qr_code_api'),
    path('api/links/<str:identifier>/qr', views.qr_code_api, name='api_qr_code_api'),

    path('links/<str:identifier>', views.link_detail_api, name='link_detail_api'),
    path('api/links/<str:identifier>', views.link_detail_api, name='api_link_detail_api'),

    # Short URL redirect at the root level
    path('<str:code>', views.redirect_short_code, name='redirect_short_code'),
]
