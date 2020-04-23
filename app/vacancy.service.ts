
import {Injectable} from '@angular/core';
import {Observable, of} from 'rxjs';
import {HttpClient} from "@angular/common/http";
import {Vacancy, LoginResponse} from "./models";

@Injectable({
  providedIn: 'root'
})
export class VacancyService {
  BASE_URL = 'http://localhost:8000'
  constructor(private http: HttpClient) {}

  getVacancyList(): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`http://localhost:8000/api/companies/${company_id}/vacancies/`);
  }
}

