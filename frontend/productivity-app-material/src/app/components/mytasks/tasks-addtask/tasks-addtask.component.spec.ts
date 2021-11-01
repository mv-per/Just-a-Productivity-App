import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TasksAddtaskComponent } from './tasks-addtask.component';

describe('TasksAddtaskComponent', () => {
  let component: TasksAddtaskComponent;
  let fixture: ComponentFixture<TasksAddtaskComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TasksAddtaskComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TasksAddtaskComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
