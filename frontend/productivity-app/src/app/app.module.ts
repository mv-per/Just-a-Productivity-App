import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import {NO_ERRORS_SCHEMA}from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from './tasks/header/header.component';
import { ButtonComponent } from './tasks/button/button.component';
import { TaskListComponent } from './tasks/task-list/task-list.component';
import { TaskItemComponent } from './tasks/task-item/task-item.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { AddTaskComponent } from './tasks/add-task/add-task.component';
import { AboutComponent } from './about/about.component';
import { FooterComponent } from './footer/footer.component';
// import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
// import { MatDatepickerModule } from '@angular/material/datepicker';
// import { MatFormFieldModule, MatInputModule } from '@angular/material';
// import {MatSelectModule} from '@angular/material/select';

const appRoutes: Routes = [
  {path: 'tasks', component: HeaderComponent},
  {path: 'about', component: AboutComponent},
]

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    ButtonComponent,
    TaskListComponent,
    TaskItemComponent,
    AddTaskComponent,
    AboutComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    FontAwesomeModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot(appRoutes),

  ],
  providers: [],
  bootstrap: [AppComponent],
  // schemas: [CUSTOM_ELEMENTS_SCHEMA, NO_ERRORS_SCHEMA]
})
export class AppModule { }
