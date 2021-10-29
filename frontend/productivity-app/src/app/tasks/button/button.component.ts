import { Component, OnInit, Input, Output, EventEmitter} from '@angular/core';
// import { EventEmitter } from 'stream';

@Component({
  selector: 'app-tasks-button',
  templateUrl: './button.component.html',
  styleUrls: ['./button.component.css']
})
export class ButtonComponent implements OnInit {
  @Input() text: string = ''; //This is what the component receives
  @Input() color: string = '';

  @Output() btnClick = new EventEmitter() //this is what the component sends
  
  constructor() { }

  ngOnInit(): void {
  }

  onClick() {
    this.btnClick.emit();
  }

}
