import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TasksHeaderComponent } from './components/mytasks/tasks-header/tasks-header.component';
import { AboutComponent } from './components/about/about.component';
import { MainPageComponent } from './components/main-page/main-page.component';

const routes: Routes = [
  {path: 'mytasks', component: TasksHeaderComponent},
  {path: 'about', component: AboutComponent},
  {path: '', component: MainPageComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
