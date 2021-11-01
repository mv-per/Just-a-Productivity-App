import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Task } from '../../../schemas/task';
import { Subscription } from 'rxjs';

import { MytaskService } from 'src/app/services/mytask.service';
import * as moment from 'moment';


export interface DialogData {
  text: string;
  day: string;
  reminder: boolean;
}

@Component({
  selector: 'app-tasks-addtask',
  templateUrl: './tasks-addtask.component.html',
  styleUrls: ['./tasks-addtask.component.css']
})
export class TasksAddtaskComponent implements OnInit {
  reminder: boolean = true;
  public taskForm!: FormGroup;
  @Output() onSubmitNewTask: EventEmitter<Task> = new EventEmitter();

  constructor(
    private formBuilder: FormBuilder,
    private dialogRef: MatDialogRef<TasksAddtaskComponent>,
    private taskService:MytaskService
  ) { }

  ngOnInit(): void {
    this.taskForm = this.formBuilder.group({
      name:['',[Validators.required]],
      day: [''],
      description:[''],
      reminder:[false]
    })
  }



  onAddTask() {
    //fix date format
    let newDate: moment.Moment = moment.utc(this.taskForm.value.day).local()
    this.taskForm.value['day'] = newDate.format("YYYY-MM-DD") + "T00:00:00";

    //add task to database and update in screen
    this.taskService.addNewTask(this.taskForm.value).subscribe((task) => this.taskService.tasks.push(task));
    this.dialogRef.close();
    this.taskForm.reset();
    // window.location.reload();
  }

  changeValue(value:boolean) {
      this.taskForm.value['reminder'] = !value;
  }

  CancelAddTask(): void {
    this.dialogRef.close();
    this.taskForm.reset();
  }

}

