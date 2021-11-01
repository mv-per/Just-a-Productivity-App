import { Component, OnInit } from '@angular/core';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {
  safeUrl!: SafeUrl;

  constructor(private _sanitizer:DomSanitizer) { }

  
  ngOnInit(): void {
    let url = "https://www.youtube.com/embed/dQw4w9WgXcQ";
    this.safeUrl = this._sanitizer.bypassSecurityTrustResourceUrl(url);
  }

}
