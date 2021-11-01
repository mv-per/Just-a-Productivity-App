import { Component, OnInit } from '@angular/core';
import { MytaskService } from 'src/app/services/mytask.service';
import { Task } from '../../../schemas/task'

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent implements OnInit {

  tasks: Task[] = [];

  constructor(public _taskService: MytaskService) { }


  getTasks(): void {
    this._taskService.getTasks().subscribe(tasks => this._taskService.tasks = tasks, err => {
      console.log(err);
    });
  }

  ngOnInit(): void {
    this.getTasks();
  }


  deleteTask(task:Task) {
    this._taskService.deleteTask(task).subscribe(
      () => this._taskService.tasks = this._taskService.tasks.filter((t) => t.id !== task.id));
    console.log(this._taskService.tasks)
  }

  updateTaskReminder(task: Task) {
    task.reminder = !task.reminder;
    this._taskService.updateReminder(task).subscribe();
  }

  // addTask(task: Task) {
  //   console.log(task);
  //   this.taskService.addNewTask(task).subscribe(
  //     (tasks) => this.taskService.tasks.push(task));
  //   // This subscribe sends the task on screen
  // }

}
