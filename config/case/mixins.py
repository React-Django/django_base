from rest_framework import renderers

from .parser import SnakeCaseParser
from .renderer import BrowsableCamelCaseRenderers, CamelCaseRenderer


class ToCamelCase(renderers.BrowsableAPIRenderer):
    renderer_classes = (BrowsableCamelCaseRenderers, CamelCaseRenderer)


class FromCamelCase:
    parser_classes = (SnakeCaseParser)
