import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogConfig, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { TasksAddtaskComponent } from '../tasks-addtask/tasks-addtask.component';


@Component({
  selector: 'app-tasks-header',
  templateUrl: './tasks-header.component.html',
  styleUrls: ['./tasks-header.component.css']
})
export class TasksHeaderComponent implements OnInit {

  title: string = "MyTasks";

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }


  openDialog() {

    const dialogConfig = new MatDialogConfig();

    // dialogConfig.disableClose = true;
    dialogConfig.autoFocus = true;
    dialogConfig.minWidth = '280px';
    dialogConfig.minHeight = '300px';
    dialogConfig.data = {
      title: 'Add a new task'
    };

    const dialogRef = this.dialog.open(TasksAddtaskComponent, dialogConfig);

    dialogRef.afterClosed().subscribe(result => {
      console.log('dialog add a new task closed', result)
    })

}


}
