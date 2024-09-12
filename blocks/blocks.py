from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class TextBlock(blocks.TextBlock):
    def  __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            help_text="Enter text in this block",
            max_length=5,
            min_length=2,
            required=False,
        )
    class Meta:
        template = "blocks/text_block.html"
        group="ikan"

class InfoBlock(blocks.StaticBlock):
    class Meta:
        admin_text = "ini namanya info block"
        label = "Info"
        template = "blocks/info_block.html"
        group="ikan"

class FAQBlock(blocks.StructBlock):
    question = blocks.CharBlock()
    answer = blocks.RichTextBlock(
        features=['bold', 'italic']
    )
class FAQListBlock(blocks.ListBlock):
    def __init__(self, **kwargs):
        super().__init__(FAQBlock(), **kwargs,)
    class Meta:
        min_num = 1
        max_num = 5
        label = "FAQ"
        template = "blocks/faq_list_block.html"

class CarouselBlock(blocks.StreamBlock):
    image = ImageChooserBlock()
    quotation = blocks.StreamBlock([
        ('text', blocks.TextBlock()),
        ('author', blocks.CharBlock()),
    ])
    class Meta:
        label = "Carousel"
        template = "blocks/carousel_block.html"

class CallToAction1Block(blocks.StructBlock):
    text = blocks.RichTextBlock(
        features=['bold', 'italic'],
        required=True,
    )
    page = blocks.PageChooserBlock()
    button_text = blocks.CharBlock(
        max_length=100,
        required=False
    )
    class Meta:
        label = "CTA #1"
        template = "blocks/call_to_action_1_block.html"

class ImageBlock(ImageChooserBlock):
    class Meta:
        template = "blocks/image_block.html"

class ParagraphBlock(blocks.RichTextBlock):
    class Meta:
        features=['bold', 'italic', 'link', 'code']
        icon="pilcrow"
        template = "blocks/paragraph_block.html"