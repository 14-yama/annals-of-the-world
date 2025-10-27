# Neo4j Audit Log Guide

## Overview
This guide explains how to implement audit logging in Neo4j using APOC triggers. Audit logs help track changes, support compliance, and ensure accountability in collaborative graph projects.

## Why Audit Logging?
- Tracks who made changes, when, and what was changed
- Supports accountability and transparency
- Enables rollback and forensic analysis
- Helps meet regulatory requirements

## Audit Log Model
Audit logs are stored as `AuditLog` nodes in Neo4j. Each log entry records:
- Timestamp
- Action type (CREATE, UPDATE, DELETE)
- Node ID and labels
- Changed properties (for updates)
- User (if available)

## Setting Up APOC Trigger for Audit Logging
APOC triggers allow you to automatically log changes to the database. The following example creates an audit log entry for every node creation, update, and deletion:

```cypher
CALL apoc.trigger.add(
  'audit_log',
  "UNWIND $createdNodes AS n
   CREATE (a:AuditLog {timestamp: timestamp(), action: 'CREATE', nodeId: id(n), labels: labels(n), properties: properties(n)})
   UNWIND $deletedNodes AS n
   CREATE (a:AuditLog {timestamp: timestamp(), action: 'DELETE', nodeId: id(n), labels: labels(n)})
   UNWIND $assignedNodeProperties AS change
   CREATE (a:AuditLog {timestamp: timestamp(), action: 'UPDATE', nodeId: id(change.node), key: change.key, old: change.old, new: change.new})",
  {phase:'after'}
)
```

### Steps to Enable Audit Logging
1. **Install APOC Procedures**
   - Ensure APOC is installed and enabled in your Neo4j instance.
2. **Add the Trigger**
   - Run the above Cypher in Neo4j Browser or via your application.
3. **Verify AuditLog Nodes**
   - After making changes (create/update/delete), query:
     ```cypher
     MATCH (a:AuditLog) RETURN a LIMIT 10
     ```
4. **Customize as Needed**
   - Add user info, relationship changes, or additional metadata as required.

## Best Practices
- Regularly review audit logs for unusual activity
- Archive or purge old logs to manage storage
- Secure access to audit logs
- Document any customizations to the trigger

## Example Query: Recent Changes
```cypher
MATCH (a:AuditLog)
RETURN a.action, a.nodeId, a.timestamp, a.key, a.old, a.new
ORDER BY a.timestamp DESC
LIMIT 20
```

## Troubleshooting
- If logs are missing, check APOC installation and trigger status
- For relationship changes, extend the trigger to handle `$createdRelationships`, `$deletedRelationships`, etc.

## References
- [APOC Documentation](https://neo4j.com/labs/apoc/)
- [Neo4j Triggers](https://neo4j.com/docs/apoc/current/trigger/)

---
*Maintaining a robust audit log is a shared responsibility. Please follow this guide and reach out to project maintainers for support or improvements.*
