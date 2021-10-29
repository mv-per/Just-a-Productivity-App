import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Task } from "../../Task"
import { faTimes } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-task-item',
  templateUrl: './task-item.component.html',
  styleUrls: ['./task-item.component.css']
})
export class TaskItemComponent implements OnInit {
  @Input() task!: Task; // It is because TypeScript 2.7 includes a strict class checking where all the properties should be initialized in the constructor. 
  // A workaround is to add the! as a postfix to the variable name
  // or add "strictPropertyInitialization": false to tsconfig.json 

  fatimes = faTimes;

  @Output() onDeleteTask: EventEmitter<Task> = new EventEmitter;
  @Output() onToggleReminder: EventEmitter<Task> = new EventEmitter;
  // isSyncAnimated:boolean = false;
  constructor() { }

  ngOnInit(): void {
  }

  onDelete(task:Task) {
    this.onDeleteTask.emit(task);
  }

  onToggle(task: Task) {
    this.onToggleReminder.emit(task)
  }


}
