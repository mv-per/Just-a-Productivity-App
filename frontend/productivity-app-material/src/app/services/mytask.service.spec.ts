import { TestBed } from '@angular/core/testing';

import { MytaskService } from './mytask.service';

describe('MytaskService', () => {
  let service: MytaskService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MytaskService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
