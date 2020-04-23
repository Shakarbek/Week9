import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NewsListComponent } from './news-list/news-list.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {FormsModule} from "@angular/forms";
import { CompanyDetailComponent } from './company-detail/company-detail.component';
import {AuthInterceptor} from "./auth.interceptor";

@NgModule({
  declarations: [
    AppComponent,
    NewsListComponent,
    CompanyDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true,
    }

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
