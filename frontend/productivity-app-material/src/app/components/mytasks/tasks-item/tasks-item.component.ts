import { Component, OnInit, Input, Output, EventEmitter} from '@angular/core';
import {Task} from '../../../schemas/task'

@Component({
  selector: 'app-tasks-item',
  templateUrl: './tasks-item.component.html',
  styleUrls: ['./tasks-item.component.css']
})
export class TasksItemComponent implements OnInit {
  @Input() task!: Task; // It is because TypeScript 2.7 includes a strict class checking where all the properties should be initialized in the constructor. 
  // A workaround is to add the! as a postfix to the variable name
  // or add "strictPropertyInitialization": false to tsconfig.json 
  @Output() onDeleteTask: EventEmitter<Task> = new EventEmitter;
  @Output() onToggleReminder: EventEmitter<Task> = new EventEmitter;

  showDetail: boolean = false;
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
