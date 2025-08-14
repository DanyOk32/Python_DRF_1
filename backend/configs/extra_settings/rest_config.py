
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.PagePagination',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'EXCEPTION_HANDLER': 'core.handlers.error_handler.error_handler',

    # 'PAGE_SIZE': 3
}
# додаємо пагінатор, путь
# якщо пагінація не потрібна можна відключити до
# конкретної Вюшки, pagination_class = None