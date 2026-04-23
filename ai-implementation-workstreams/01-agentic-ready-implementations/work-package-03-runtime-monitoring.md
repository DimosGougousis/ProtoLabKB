# Work Package 03: Runtime Monitoring & Behavioral Analysis

## Status: 🤖 AGENTIC-READY - Can Start Immediately

**Work Package ID:** WP-AI-003  
**Priority:** P1 - High  
**Timeline:** 7 business days  
**Owner:** AI Operations Team  
**Effort:** 1 engineer × 1.5 weeks

---

## 1. Objectives

Deploy comprehensive runtime monitoring that:
- Monitors AI system behavior in real-time
- Detects anomalies and suspicious patterns
- Tracks user behavior for insider threat detection
- Provides alerting and incident response
- Maintains audit trails for compliance

---

## 2. Deliverables

| Deliverable | Description | Acceptance Criteria |
|-------------|-------------|---------------------|
| **D1: Monitoring Agent** | Python-based monitoring service | Deployed, collecting metrics from all AI services |
| **D2: Anomaly Detection** | ML-based anomaly detection | >90% anomaly detection, <5% false positive rate |
| **D3: Behavioral Analytics** | User behavior tracking | 100% user activity coverage, behavioral baselines established |
| **D4: Alerting System** | Real-time alerting | <30 second alert latency, 100% critical alert coverage |
| **D5: Monitoring Dashboard** | Grafana/Prometheus dashboard | Real-time visibility, historical trends, drill-down capability |
| **D6: Audit Logging** | Comprehensive audit trail | 100% coverage, 7-year retention, tamper-evident |

---

## 3. Technical Implementation

### 3.1 Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         AI SERVICES                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │   DFM       │  │   Material  │  │   CNC       │  │   3D Print  │          │
│  │   Analyzer  │  │   Selector  │  │   Optimizer │  │   Advisor   │          │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘          │
└─────────┼────────────────┼────────────────┼────────────────┼─────────────────┘
          │                │                │                │
          └────────────────┴────────────────┴────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      MONITORING AGENT                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Metrics Collection                                                  │  │
│  │  - Request/response logging                                         │  │
│  │  - Latency tracking                                                 │  │
│  │  - Error rate monitoring                                          │  │
│  │  - Token usage tracking                                             │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Anomaly Detection                                                   │  │
│  │  - Statistical anomaly detection                                    │  │
│  │  - ML-based anomaly detection                                       │  │
│  │  - Baseline deviation detection                                     │  │
│  │  - Time-series analysis                                             │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Behavioral Analytics                                                │  │
│  │  - User behavior profiling                                          │  │
│  │  - Session analysis                                                 │  │
│  │  - Peer group analysis                                              │  │
│  │  - Insider threat indicators                                        │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      OBSERVABILITY STACK                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │ Prometheus  │  │   Grafana   │  │    ELK      │  │  PagerDuty  │          │
│  │  (Metrics)  │  │(Dashboards) │  │   (Logs)    │  │  (Alerts)   │          │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Implementation Code

```python
# runtime_monitoring_agent.py
# Deployable immediately via agentic workflow

import json
import time
import hashlib
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta
from collections import defaultdict
import statistics
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class MetricSnapshot:
    """Snapshot of system metrics"""
    timestamp: str
    service_name: str
    request_count: int
    error_count: int
    latency_p50: float
    latency_p95: float
    latency_p99: float
    token_count: int
    unique_users: int


@dataclass
class AnomalyAlert:
    """Anomaly detection alert"""
    alert_id: str
    timestamp: str
    anomaly_type: str
    severity: str
    service_name: str
    description: str
    metric_value: float
    baseline_value: float
    deviation_percent: float
    recommended_action: str


@dataclass
class BehaviorProfile:
    """User behavior profile"""
    user_id: str
    created_at: str
    last_updated: str
    request_count: int
    avg_requests_per_day: float
    typical_hours: List[int]
    common_services: List[str]
    avg_latency: float
    error_rate: float
    peer_group: str
    risk_score: int


class RuntimeMonitoringAgent:
    """
    Runtime monitoring and behavioral analysis for manufacturing AI
    Deployable immediately via agentic workflow
    """
    
    def __init__(self, config: dict = None):
        self.config = config or {}
        
        # Metrics storage (in production: use time-series database)
        self.metrics_history: List[MetricSnapshot] = []
        self.user_profiles: Dict[str, BehaviorProfile] = {}
        self.anomaly_alerts: List[AnomalyAlert] = []
        
        # Configuration
        self.anomaly_threshold = self.config.get('anomaly_threshold', 2.0)  # Standard deviations
        self.baseline_window_days = self.config.get('baseline_window_days', 7)
        self.alert_retention_days = self.config.get('alert_retention_days', 90)
        
        # Service tracking
        self.service_metrics: Dict[str, List[dict]] = defaultdict(list)
        self.user_activity: Dict[str, List[dict]] = defaultdict(list)
    
    def record_request(self, service_name: str, user_id: str,
                       latency_ms: float, tokens: int,
                       error: bool = False, request_data: dict = None) -> dict:
        """
        Record a request for monitoring
        
        Args:
            service_name: Name of AI service
            user_id: User identifier
            latency_ms: Request latency in milliseconds
            tokens: Token count
            error: Whether request resulted in error
            request_data: Additional request data
            
        Returns:
            Monitoring result with anomaly detection
        """
        timestamp = datetime.utcnow()
        
        # Record in service metrics
        metric_record = {
            'timestamp': timestamp.isoformat(),
            'user_id': user_id,
            'latency_ms': latency_ms,
            'tokens': tokens,
            'error': error
        }
        self.service_metrics[service_name].append(metric_record)
        
        # Record user activity
        user_record = {
            'timestamp': timestamp.isoformat(),
            'service_name': service_name,
            'latency_ms': latency_ms,
            'tokens': tokens,
            'error': error
        }
        self.user_activity[user_id].append(user_record)
        
        # Update user behavior profile
        self._update_user_profile(user_id)
        
        # Check for anomalies
        anomalies = self._detect_anomalies(service_name, user_id, metric_record)
        
        # Generate alerts for critical anomalies
        alerts = []
        for anomaly in anomalies:
            if anomaly['severity'] in ['high', 'critical']:
                alert = self._create_alert(anomaly, service_name)
                alerts.append(alert)
                self.anomaly_alerts.append(alert)
        
        return {
            'recorded': True,
            'anomalies_detected': len(anomalies),
            'alerts_generated': len(alerts),
            'user_profile_updated': True,
            'timestamp': timestamp.isoformat()
        }
    
    def get_metrics(self, service_name: str = None, 
                   timeframe_hours: int = 24) -> MetricSnapshot:
        """Get metrics snapshot for specified timeframe"""
        
        cutoff = datetime.utcnow() - timedelta(hours=timeframe_hours)
        
        if service_name:
            records = [
                r for r in self.service_metrics[service_name]
                if datetime.fromisoformat(r['timestamp']) > cutoff
            ]
        else:
            records = []
            for service_records in self.service_metrics.values():
                records.extend([
                    r for r in service_records
                    if datetime.fromisoformat(r['timestamp']) > cutoff
                ])
        
        if not records:
            return MetricSnapshot(
                timestamp=datetime.utcnow().isoformat(),
                service_name=service_name or 'all',
                request_count=0,
                error_count=0,
                latency_p50=0,
                latency_p95=0,
                latency_p99=0,
                token_count=0,
                unique_users=0
            )
        
        # Calculate metrics
        latencies = [r['latency_ms'] for r in records]
        errors = [r for r in records if r['error']]
        tokens = [r['tokens'] for r in records]
        users = set(r['user_id'] for r in records)
        
        return MetricSnapshot(
            timestamp=datetime.utcnow().isoformat(),
            service_name=service_name or 'all',
            request_count=len(records),
            error_count=len(errors),
            latency_p50=statistics.median(latencies),
            latency_p95=sorted(latencies)[int(len(latencies) * 0.95)],
            latency_p99=sorted(latencies)[int(len(latencies) * 0.99)],
            token_count=sum(tokens),
            unique_users=len(users)
        )
    
    def get_user_profile(self, user_id: str) -> Optional[BehaviorProfile]:
        """Get behavior profile for user"""
        return self.user_profiles.get(user_id)
    
    def get_alerts(self, severity: str = None, 
                   since_hours: int = 24) -> List[AnomalyAlert]:
        """Get anomaly alerts"""
        cutoff = datetime.utcnow() - timedelta(hours=since_hours)
        
        alerts = [
            a for a in self.anomaly_alerts
            if datetime.fromisoformat(a.timestamp) > cutoff
        ]
        
        if severity:
            alerts = [a for a in alerts if a.severity == severity]
        
        return alerts
    
    def _update_user_profile(self, user_id: str):
        """Update behavior profile for user"""
        
        activity = self.user_activity.get(user_id, [])
        if not activity:
            return
        
        # Calculate profile metrics
        now = datetime.utcnow()
        
        # Request count
        request_count = len(activity)
        
        # Average requests per day
        if len(activity) >= 2:
            first_activity = datetime.fromisoformat(activity[0]['timestamp'])
            days_active = max(1, (now - first_activity).days)
            avg_requests_per_day = request_count / days_active
        else:
            avg_requests_per_day = request_count
        
        # Typical hours
        hours = [datetime.fromisoformat(a['timestamp']).hour for a in activity]
        typical_hours = list(set(hours)) if hours else []
        
        # Common services
        services = [a['service_name'] for a in activity]
        common_services = list(set(services)) if services else []
        
        # Average latency
        latencies = [a['latency_ms'] for a in activity]
        avg_latency = statistics.mean(latencies) if latencies else 0
        
        # Error rate
        errors = [a for a in activity if a.get('error', False)]
        error_rate = len(errors) / request_count if request_count > 0 else 0
        
        # Peer group (simplified - would use clustering in production)
        if avg_requests_per_day > 100:
            peer_group = "power_user"
        elif avg_requests_per_day > 10:
            peer_group = "regular_user"
        else:
            peer_group = "occasional_user"
        
        # Risk score (simplified)
        risk_score = 0
        if error_rate > 0.1:
            risk_score += 20
        if avg_requests_per_day > 1000:
            risk_score += 15
        if len(typical_hours) > 12:  # Unusual hour distribution
            risk_score += 10
        
        # Create or update profile
        self.user_profiles[user_id] = BehaviorProfile(
            user_id=user_id,
            created_at=self.user_profiles.get(user_id, BehaviorProfile(
                user_id=user_id, created_at=now.isoformat(),
                last_updated=now.isoformat(), request_count=0,
                avg_requests_per_day=0, typical_hours=[],
                common_services=[], avg_latency=0, error_rate=0,
                peer_group="unknown", risk_score=0
            )).created_at if user_id in self.user_profiles else now.isoformat(),
            last_updated=now.isoformat(),
            request_count=request_count,
            avg_requests_per_day=round(avg_requests_per_day, 2),
            typical_hours=typical_hours,
            common_services=common_services,
            avg_latency=round(avg_latency, 2),
            error_rate=round(error_rate, 4),
            peer_group=peer_group,
            risk_score=risk_score
        )
    
    def _detect_anomalies(self, service_name: str, user_id: str, 
                          metric_record: dict) -> List[dict]:
        """Detect anomalies in metrics"""
        
        anomalies = []
        
        # Get user profile
        profile = self.user_profiles.get(user_id)
        if not profile:
            return anomalies
        
        # Check for latency anomaly
        current_latency = metric_record['latency_ms']
        if current_latency > profile.avg_latency * 3:
            anomalies.append({
                'type': 'latency_spike',
                'severity': 'medium',
                'description': f"Latency {current_latency}ms exceeds 3x baseline {profile.avg_latency}ms",
                'metric_value': current_latency,
                'baseline_value': profile.avg_latency,
                'deviation_percent': ((current_latency - profile.avg_latency) / profile.avg_latency) * 100
            })
        
        # Check for error rate anomaly
        if metric_record.get('error', False):
            # Check if user has elevated error rate
            if profile.error_rate > 0.1:  # >10% error rate
                anomalies.append({
                    'type': 'elevated_error_rate',
                    'severity': 'high',
                    'description': f"User error rate {profile.error_rate:.2%} exceeds threshold",
                    'metric_value': profile.error_rate,
                    'baseline_value': 0.05,
                    'deviation_percent': (profile.error_rate / 0.05) * 100
                })
        
        # Check for unusual hour activity
        current_hour = datetime.utcnow().hour
        if profile.typical_hours and current_hour not in profile.typical_hours:
            anomalies.append({
                'type': 'unusual_hour_activity',
                'severity': 'low',
                'description': f"Activity at hour {current_hour} outside typical hours {profile.typical_hours}",
                'metric_value': current_hour,
                'baseline_value': profile.typical_hours[0] if profile.typical_hours else 0,
                'deviation_percent': 100
            })
        
        # Check for volume anomaly
        recent_requests = len([
            r for r in self.user_activity.get(user_id, [])
            if (datetime.utcnow() - datetime.fromisoformat(r['timestamp'])).total_seconds() < 3600
        ])
        
        if recent_requests > profile.avg_requests_per_day / 24 * 10:  # 10x hourly average
            anomalies.append({
                'type': 'volume_spike',
                'severity': 'medium',
                'description': f"{recent_requests} requests in last hour exceeds baseline",
                'metric_value': recent_requests,
                'baseline_value': profile.avg_requests_per_day / 24,
                'deviation_percent': (recent_requests / (profile.avg_requests_per_day / 24)) * 100
            })
        
        return anomalies
    
    def _create_alert(self, anomaly: dict, service_name: str) -> AnomalyAlert:
        """Create an alert from anomaly"""
        
        severity_map = {
            'critical': 'critical',
            'high': 'high',
            'medium': 'medium',
            'low': 'low'
        }
        
        return AnomalyAlert(
            alert_id=self._generate_request_id(),
            timestamp=datetime.utcnow().isoformat(),
            anomaly_type=anomaly['type'],
            severity=severity_map.get(anomaly['severity'], 'low'),
            service_name=service_name,
            description=anomaly['description'],
            metric_value=anomaly['metric_value'],
            baseline_value=anomaly['baseline_value'],
            deviation_percent=anomaly['deviation_percent'],
            recommended_action=self._get_recommended_action(anomaly)
        )
    
    def _get_recommended_action(self, anomaly: dict) -> str:
        """Get recommended action for anomaly"""
        
        action_map = {
            'latency_spike': 'Investigate service performance, check for resource constraints',
            'elevated_error_rate': 'Review error logs, check for service degradation or attacks',
            'unusual_hour_activity': 'Review user activity, verify legitimate business need',
            'volume_spike': 'Check for DDoS or scraping activity, consider rate limiting',
            'insider_threat_indicator': 'Escalate to security team, preserve evidence',
            'data_exfiltration_attempt': 'Block user immediately, initiate incident response'
        }
        
        return action_map.get(anomaly['type'], 'Review and investigate')


# DEPLOYMENT INSTRUCTIONS
# =========================

# 1. Deploy Monitoring Agent (Days 1-2)
#    - Install monitoring agent on all AI service hosts
#    - Configure metric collection endpoints
#    - Set up log aggregation

# 2. Configure Anomaly Detection (Days 3-4)
#    - Establish behavioral baselines
#    - Configure anomaly thresholds
#    - Test detection accuracy

# 3. Set Up Alerting (Days 5-6)
#    - Configure alert routing
#    - Set up PagerDuty integration
#    - Test alert delivery

# 4. Deploy Dashboards (Day 7)
#    - Deploy Grafana dashboards
#    - Configure Prometheus metrics
#    - Verify data flow

# SUCCESS CRITERIA
# ================
# - 100% of AI services monitored
# - <30 second alert latency
# - >90% anomaly detection rate
# - <5% false positive rate
# - 100% audit coverage
# - 99.9% monitoring uptime

# MONITORING COVERAGE REQUIREMENTS
# ================================
# - All AI service endpoints
# - All user interactions
# - All data access events
# - All configuration changes
# - All authentication events
# - All authorization decisions
```

---

## 4. Operational Runbook

### 4.1 Daily Operations

**Morning Checks (9:00 AM):**
```bash
# Check monitoring system health
curl http://monitoring-agent:8080/health

# Review overnight alerts
monitoring-cli alerts --since "24 hours ago" --severity high,critical

# Check anomaly detection status
monitoring-cli anomalies --status active

# Review dashboard health
monitoring-cli dashboards --check
```

**Evening Checks (5:00 PM):**
```bash
# Review day's metrics
monitoring-cli summary --date today

# Check for trending issues
monitoring-cli trends --timeframe 24h

# Verify alert delivery
monitoring-cli alerts --verify-delivery

# Check data retention
monitoring-cli storage --status
```

### 4.2 Alert Response Procedures

**Critical Alert Response:**
```
1. Acknowledge alert within 5 minutes
2. Assess severity and impact
3. Execute response playbook
4. Notify stakeholders
5. Document actions taken
6. Schedule post-incident review
```

**High Priority Alert Response:**
```
1. Acknowledge alert within 15 minutes
2. Investigate root cause
3. Take corrective action
4. Document findings
5. Update baselines if needed
```

**Medium/Low Priority Alert Response:**
```
1. Review during business hours
2. Assess if tuning needed
3. Update thresholds if appropriate
4. Document in daily log
```

---

## 5. Success Metrics

### 5.1 Key Performance Indicators

| Metric | Target | Measurement |
|--------|--------|-------------|
| Monitoring Coverage | 100% | Percentage of AI services monitored |
| Alert Latency | <30 seconds | Time from anomaly to alert |
| Anomaly Detection Rate | >90% | True anomalies detected / Total anomalies |
| False Positive Rate | <5% | False positives / Total alerts |
| Dashboard Availability | 99.9% | Uptime percentage |
| Data Retention | 100% | Compliance with retention policy |

### 5.2 Operational Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Mean Time to Detect (MTTD) | <5 minutes | Time from incident to detection |
| Mean Time to Alert (MTTA) | <30 seconds | Time from detection to alert |
| Mean Time to Respond (MTTR) | <15 minutes | Time from alert to response |
| Alert Acknowledgment Rate | >95% | Alerts acknowledged within SLA |
| False Positive Resolution | <24 hours | Time to resolve false positives |

---

## 6. Deployment Checklist

### Pre-Deployment

- [ ] Infrastructure provisioned
- [ ] Dependencies installed
- [ ] Configuration validated
- [ ] SSL/TLS certificates installed
- [ ] Database connections tested
- [ ] Prometheus endpoint configured
- [ ] Grafana dashboards created
- [ ] Alerting rules defined
- [ ] PagerDuty integration tested

### Deployment

- [ ] Code deployed to staging
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] Performance tests passing
- [ ] Configuration validated in staging
- [ ] Rollback procedure tested
- [ ] Documentation updated

### Production

- [ ] Maintenance window scheduled
- [ ] Stakeholders notified
- [ ] Production deployment executed
- [ ] Health checks passing
- [ ] Smoke tests executed
- [ ] Monitoring verified
- [ ] Alerting verified
- [ ] 24-hour monitoring completed

---

## 7. Approval

### Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Work Package Owner | | | |
| Engineering Lead | | | |
| Security Lead | | | |
| Product Manager | | | |
| QA Lead | | | |

### Approval Status

- [ ] Technical Review Complete
- [ ] Security Review Complete
- [ ] Architecture Review Complete
- [ ] Cost Review Complete
- [ ] Risk Assessment Complete
- [ ] Dependencies Verified
- [ ] Ready for Implementation

---

**Document Owner:** AI Operations Team  
**Last Updated:** April 23, 2026  
**Next Review:** Weekly during implementation  
**Classification:** Internal Use - Implementation Plan
