from carbon_alt_delete.client.module_interface import ModuleInterface
from comments.comment_model_interface import CommentModelInterface


class CommentsModuleInterface(ModuleInterface):
    def __init__(self, client):
        super().__init__("comments", "v1")
        self.comments: CommentModelInterface = CommentModelInterface(client=client, module=self)
