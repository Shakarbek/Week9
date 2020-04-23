import { Component, OnInit } from '@angular/core';
import {Company, Vacancy} from '../models'
import {CompanyService} from '../company.service'
import { ActivatedRoute } from '@angular/router';
import {VacancyService} from '../vacancy.service'

@Component({
  selector: 'app-company-detail',
  templateUrl: './company-detail.component.html',
  styleUrls: ['./company-detail.component.css']
})
export class CompanyDetailComponent implements OnInit {
  vacancy: Vacancy;

  constructor(private vacancyService: VacancyService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getVacancy();
  }
  getVacancy() {
    const id = +this.route.snapshot.paramMap.get('company_id');
    this.vacancyService.getVacancyList.get(vacancy => this.vacancy = vacancy);
  }


}
