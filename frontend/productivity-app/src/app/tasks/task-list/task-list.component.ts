import { Component, OnInit } from '@angular/core';
import { TaskService } from '../../services/task.service';
import { Task } from "../../Task"

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {

  tasks!: Task[];

  constructor(private taskService: TaskService) { }

  ngOnInit(): void {
    this.taskService.getTasks().subscribe((tasks) => this.tasks = tasks);
  }

  deleteTask(task:Task) {
    this.taskService.deleteTask(task).subscribe(
      () => this.tasks = this.tasks.filter((t) => t.id !== task.id));
  }

  updateTaskReminder(task: Task) {
    task.reminder = !task.reminder;
    this.taskService.updateReminder(task).subscribe();
  }

  addTask(task: Task) {
    console.log(task);
    this.taskService.addNewTask(task).subscribe(
      (tasks) => this.tasks.push(task));
    // This subscribe sends the task on screen
  }
}
