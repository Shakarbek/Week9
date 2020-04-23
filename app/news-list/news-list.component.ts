import { Component, OnInit } from '@angular/core';
import {CompanyService} from "../company.service";
import {Company} from "../models";

@Component({
  selector: 'app-news-list',
  templateUrl: './news-list.component.html',
  styleUrls: ['./news-list.component.css']
})
export class NewsListComponent implements OnInit {
  companies: Company[] = [];

  constructor(public companyService: CompanyService) { }

  ngOnInit(): void {
    this.getCompanyList();
  }

  getCompanyList() {
    const newsObservable = this.companyService.getCompanyList().subscribe( companies => this.companies = companies);

  };

}


