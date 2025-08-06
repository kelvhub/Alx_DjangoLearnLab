# Permissions and Groups Setup for Bookshelf App

## Custom Model Permissions

Defined in `Book` model:
- can_view: Can view book
- can_create: Can create book
- can_edit: Can edit book
- can_delete: Can delete book

## Groups and Their Permissions

- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: All permissions

## How Permissions Are Enforced

Views are protected using Django's `@permission_required` decorator.

Example:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
