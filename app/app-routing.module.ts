import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NewsListComponent } from './news-list/news-list.component';
import { CompanyDetailComponent } from './company-detail/company-detail.component';


const routes: Routes = [
  { path: '', component: NewsListComponent },
  { path: 'company/:id/vacancies/', component: CompanyDetailComponent }
  ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
