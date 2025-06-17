# 🔄 Agent Funnel Assignment System

A system that assigns eligible `wafunnel` records to active `agents` using a **SQL Server stored procedure**. The assignment is triggered automatically every day at **8:40 PM** via a **Flask API with APScheduler**, and can also be manually triggered via a REST endpoint.

---

## 📋 Features

- ✅ Even distribution of eligible `wafunnel` entries to active agents
- ⏱️ Auto-scheduled execution (daily at 8:40 PM)
- 🖱️ Manual HTTP trigger (`/run-now`)
- ⚠️ Ensures no agent receives more than **450 records**
- 🔗 Integration with Microsoft SQL Server using `pymssql`
- 🧪 Easily testable with Flask

---

## 🗃️ Database Schema Overview

### `agents`
| Column  | Type     | Description             |
|---------|----------|-------------------------|
| agent   | VARCHAR  | Unique agent ID         |
| status  | VARCHAR  | 'active' or 'inactive'  |

### `wafunnel`
| Column | Type      | Description                             |
|--------|-----------|-----------------------------------------|
| number | VARCHAR   | Phone number                            |
| stage  | INT       | Funnel status (1 to 4)                  |
| date   | DATETIME  | Date the funnel record was created      |

### `agent_wafunnel_assignment`
| Column | Type     | Description                |
|--------|----------|----------------------------|
| agent  | VARCHAR  | Assigned agent ID          |
| number | VARCHAR  | Assigned funnel record     |

---

## 🧠 Stored Procedure: `sp_assign_wafunnel_to_agents`

### ✅ Purpose

Distributes eligible `wafunnel` records evenly among all **active agents**, with the following rules:

- Only records with `stage < 4` and `date >= today - 45 days` are considered
- Each active agent is assigned a roughly equal share
- Each agent gets **no more than 450 records**
- Assigned records have their `stage` incremented by 1
- Existing assignments are cleared before new ones are applied

---

### 📜 Full Logic Breakdown

1. **Delete all existing assignments**
   - Truncates the `agent_wafunnel_assignment` table

2. **Select active agents**
   - Filters `agents` table where `status = 'active'`
   - Stores them with a row number for mapping

3. **Select eligible funnel records**
   - From `wafunnel` where:
     - `stage < 4`
     - `date >= current date - 45 days`

4. **Calculate records to assign per agent**
   - `assign_per_agent = CEIL(total_eligible / total_active_agents)`
   - If `assign_per_agent > 450`, it's capped at 450

5. **Calculate total assignable rows**
   - Total = `assign_per_agent × number of active agents`
   - If this is more than available, it's trimmed to available

6. **Assign records to agents**
   - Row-number based distribution (1st set to 1st agent, etc.)

7. **Update funnel `stage`**
   - Each assigned record's `stage` is incremented by 1
   - If `stage = 3`, it becomes `4` (max)

---

### ⚙️ Run Manually (SQL Server)

```sql
EXEC sp_assign_wafunnel_to_agents;