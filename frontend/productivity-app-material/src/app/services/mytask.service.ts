import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable, throwError} from 'rxjs';
import { Task } from '../schemas/task';

import { map, catchError } from 'rxjs/operators';

 

@Injectable({
  providedIn: 'root'
})
export class MytaskService {


  tasks: Task[] = [];

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
    })
  }

  private apiUrl = 'api/tasks/'; //The tasks api is running on this endpoint
  

  constructor(private httpRequests: HttpClient) {
  }

  getTasks(): Observable<Task[]> {
    return this.httpRequests.get<Task[]>(this.apiUrl)
  }

  ngOnInit(): void {
    this.getTasks().subscribe((tasks:Task[]) => this.tasks = tasks) 
  }

  deleteTask(task: Task): Observable<Task> {
    return this.httpRequests.delete<Task>(this.apiUrl + task.id, this.httpOptions)
  }

  updateReminder(task: Task): Observable<Task> {
    console.log(task.id, task);
    return this.httpRequests.put<Task>(this.apiUrl + task.id, task, this.httpOptions)
  }

  addNewTask(task: Task): Observable<Task> {
    //Store in local file, so it can be seen in other components
    // this.tasks.push(task);
    //send to database through API
    return this.httpRequests.post<Task>(this.apiUrl, task, this.httpOptions)
  }

  
}