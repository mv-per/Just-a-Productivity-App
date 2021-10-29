import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable,  of} from 'rxjs';
import {Task} from "../Task"

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
  })
}

@Injectable({
  providedIn: 'root'
})
export class TaskService {

  

  private apiUrl = 'api/tasks/'; //The tasks api is running on this endpoint
  

  constructor(private http:HttpClient) { }

  getTasks(): Observable<Task[]> {
    console.log(this.apiUrl)
    return this.http.get<Task[]>(this.apiUrl)
  }

  deleteTask(task: Task): Observable<Task> {
    const url_with_id = `${this.apiUrl}${task.id}`;
    return this.http.delete<Task>(url_with_id, httpOptions)
  }

  updateReminder(task: Task): Observable<Task> {
    const url_with_id = `${this.apiUrl}${task.id}`;
    console.log(task.id, task);
    return this.http.put<Task>(url_with_id, task, httpOptions)
  }

  addNewTask(task: Task): Observable<Task> {
    return this.http.post<Task>(this.apiUrl, task, httpOptions)
  }
  // addTask(task: Task): Observable<Task> {
  //   let headers = new HttpHeaders().append('Content-Type', 'application/json')
  //   // const url_with_id = `${this.apiUrl};
  //   return this.http.post<Task>(url_with_id, {headers: headers})
  // }
}
