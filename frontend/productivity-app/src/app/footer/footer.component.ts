import { Component, OnInit } from '@angular/core';

import { faListAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
  falist = faListAlt;
  constructor() { }

  ngOnInit(): void {
  }

}
