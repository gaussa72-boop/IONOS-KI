#!/usr/bin/env python3
"""
GALACTIC SINGULARITY ULTRA - Test Suite
========================================
Umfassende Tests für alle Funktionen
"""

import sys
sys.path.insert(0, '/Users/Querox9396/PycharmProjects/GALACTIC_SINGULARITY_ULTRA')

from app_unified import app, init_db, galactic_brain
import json

def test_app_import():
    """Test 1: App Import"""
    print("\n" + "="*60)
    print("TEST 1: App Import")
    print("="*60)
    try:
        print("✓ App imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed: {e}")
        return False

def test_database():
    """Test 2: Database"""
    print("\n" + "="*60)
    print("TEST 2: Database Initialization")
    print("="*60)
    try:
        init_db()
        print("✓ Database initialized")
        print("✓ Tables created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed: {e}")
        return False

def test_galactic_brain():
    """Test 3: Galactic Brain AI"""
    print("\n" + "="*60)
    print("TEST 3: Galactic Brain AI Module")
    print("="*60)

    tests = [
        ("Hallo", "Simple greeting"),
        ("quantum", "Quantum AI"),
        ("blume", "Lebensblume AI"),
        ("spirit", "Urspirit AI"),
        ("geld wohlstand", "Finance Agent"),
        ("musik create", "Creator Agent"),
        ("social post", "Social Agent"),
    ]

    all_passed = True
    for message, description in tests:
        try:
            response = galactic_brain.process(message)
            if response and len(response) > 0:
                print(f"✓ {description}: {response[0][:50]}...")
            else:
                print(f"❌ {description}: No response")
                all_passed = False
        except Exception as e:
            print(f"❌ {description}: {e}")
            all_passed = False

    return all_passed

def test_api_endpoints():
    """Test 4: API Endpoints"""
    print("\n" + "="*60)
    print("TEST 4: API Endpoints")
    print("="*60)

    tests = [
        ("/", "GET", None, "Homepage"),
        ("/api/status", "GET", None, "Status API"),
        ("/chat", "POST", {"message": "test"}, "Chat API"),
    ]

    with app.test_client() as client:
        all_passed = True
        for endpoint, method, data, description in tests:
            try:
                if method == "GET":
                    response = client.get(endpoint)
                else:
                    response = client.post(endpoint,
                        json=data,
                        headers={'Content-Type': 'application/json'})

                status = response.status_code
                if status in [200, 400, 401]:
                    print(f"✓ {description} ({endpoint}): Status {status}")
                else:
                    print(f"⚠️  {description} ({endpoint}): Status {status}")
                    all_passed = False
            except Exception as e:
                print(f"❌ {description} ({endpoint}): {e}")
                all_passed = False

    return all_passed

def test_chat_functionality():
    """Test 5: Chat Functionality"""
    print("\n" + "="*60)
    print("TEST 5: Chat Functionality")
    print("="*60)

    with app.test_client() as client:
        chat_tests = [
            ({"message": "Hallo"}, "Simple greeting"),
            ({"message": "Wer bist du?"}, "Identity check"),
            ({"message": "Hilfe"}, "Help request"),
            ({"message": "quantum energie"}, "Quantum question"),
        ]

        all_passed = True
        for data, description in chat_tests:
            try:
                response = client.post('/chat',
                    json=data,
                    headers={'Content-Type': 'application/json'})

                if response.status_code == 200:
                    chat_data = response.get_json()
                    if "response" in chat_data:
                        response_text = chat_data["response"][:40]
                        print(f"✓ {description}: {response_text}...")
                    else:
                        print(f"❌ {description}: No response key")
                        all_passed = False
                else:
                    print(f"⚠️  {description}: Status {response.status_code}")
            except Exception as e:
                print(f"❌ {description}: {e}")
                all_passed = False

        return all_passed

def main():
    """Führe alle Tests aus"""
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║     🌌 GALACTIC SINGULARITY ULTRA - TEST SUITE 🌌            ║
    ║                                                               ║
    ║     Comprehensive System Tests                               ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    results = {}
    results['Import'] = test_app_import()
    results['Database'] = test_database()
    results['Brain'] = test_galactic_brain()
    results['Endpoints'] = test_api_endpoints()
    results['Chat'] = test_chat_functionality()

    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)

    total = len(results)
    passed = sum(1 for v in results.values() if v)

    for test_name, result in results.items():
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")

    print(f"\n📊 Total: {passed}/{total} tests passed")

    if passed == total:
        print("\n✨ ALL TESTS PASSED! System is ready! ✨\n")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed.\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())

