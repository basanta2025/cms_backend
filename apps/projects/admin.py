from django.contrib import admin

# Register your models here.
from .models import (
    BudgetCategory,
    Company,
    Document,
    Milestone,
    MilestoneStatus,
    Project,
    ProjectBudget,
    ProjectStatus,
    Task,
    TaskProgressLog,
    TaskStatus,
)

admin.site.register(
    [
        BudgetCategory,
        Company,
        Document,
        Milestone,
        # MilestoneStatus,
        Project,
        ProjectBudget,
        # ProjectStatus,
        Task,
        TaskProgressLog,
        # TaskStatus,
    ]
)
