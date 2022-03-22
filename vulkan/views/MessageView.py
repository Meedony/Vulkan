from Vulkan.Views.AbstractView import AbstractView
from Vulkan.Controllers.ControllerResponse import ControllerResponse


class MessageView(AbstractView):
    def __init__(self, response: ControllerResponse) -> None:
        super().__init__(response)

    async def run(self) -> None:
        return super().run()