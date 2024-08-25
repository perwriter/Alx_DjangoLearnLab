# Permission and Group Setup

## Custom Permissions
- `can_view`: Allows viewing of a document.
- `can_create`: Allows creating a new document.
- `can_edit`: Allows editing an existing document.
- `can_delete`: Allows deleting a document.

## Groups and Assigned Permissions
- `Viewers`: Can view documents.
- `Editors`: Can view, create, and edit documents.
- `Admins`: Can perform all actions (view, create, edit, delete).

## Enforcing Permissions
Permissions are enforced in views using the `@permission_required` decorator to ensure that only users with the appropriate permissions can access specific functionality.
