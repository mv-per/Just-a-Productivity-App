//Angular Modules
import { NgModule } from '@angular/core';
import { BrowserModule, DomSanitizer } from '@angular/platform-browser';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
// import { MatIconButtonModule } from '@angular/material/button';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTooltipModule } from '@angular/material/tooltip';
import {MatFormFieldModule} from '@angular/material/form-field';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MAT_DATE_FORMATS } from '@angular/material/core';
import { MatNativeDateModule } from '@angular/material/core';
import { MatMomentDateModule } from '@angular/material-moment-adapter';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { YouTubePlayerModule } from '@angular/youtube-player';
import { MatDialogModule, MatDialogRef } from '@angular/material/dialog';



//Local components
import { MainHeaderComponent } from './components/main-header/main-header.component';
import { FooterComponent } from './components/footer/footer.component';
import { TasksHeaderComponent } from './components/mytasks/tasks-header/tasks-header.component';
import { TasksItemComponent } from './components/mytasks/tasks-item/tasks-item.component';
import { TasksAddtaskComponent } from './components/mytasks/tasks-addtask/tasks-addtask.component'
import { TasksComponent } from './components/mytasks/tasks/tasks.component'

import { MY_DATE_FORMATS } from './my-date-formats';
import { AboutComponent } from './components/about/about.component';
import { MainPageComponent } from './components/main-page/main-page.component';


@NgModule({
  declarations: [
    AppComponent,
    MainHeaderComponent,
    FooterComponent,
    AboutComponent,
    TasksComponent,
    TasksHeaderComponent,
    TasksItemComponent,
    TasksAddtaskComponent,
    MainPageComponent,
    ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatIconModule,
    HttpClientModule,
    MatToolbarModule,
    MatTooltipModule,
    MatDialogModule,
    MatFormFieldModule,
    FormsModule,
    ReactiveFormsModule,
    MatInputModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatCheckboxModule,
    MatMomentDateModule,
    YouTubePlayerModule,
  ],
  providers: [ { provide: MatDialogRef, useValue: {}}, {provide:MAT_DIALOG_DATA,useValue:{}},
    {
      provide: MAT_DATE_FORMATS,
      useValue: MY_DATE_FORMATS
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
