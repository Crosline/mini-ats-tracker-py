# from drf_spectacular.extensions import OpenApiViewExtension
# from rest_framework import viewsets

# class AutoTagViewExtension(OpenApiViewExtension):
#     """
#     Automatically assign a tag to all ModelViewSets
#     based on the class name (removing 'ViewSet').
#     """
#     target_class = viewsets.ModelViewSet  # applies to all ModelViewSets

#     def view_replacement(self):
#         # Set the tags for this ViewSet
#         print("AAAAAAAAAAAAAAAAAAAA")
#         tag_name = self.view.__class__.__name__
#         if tag_name.endswith("ViewSet"):
#             tag_name = tag_name[:-7]  # remove 'ViewSet' suffix
#         self.tags = [tag_name]
#         return self.view
