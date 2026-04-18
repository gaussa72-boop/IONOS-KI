#!/usr/bin/env python3
"""
GALACTIC SINGULARITY ULTRA - Integration Test
==============================================
Testet alle Module und die Flask App
"""

import sys
import os

# Add path
sys.path.insert(0, os.path.dirname(__file__))

def test_imports():
    """Test 1: Module Imports"""
    print("\n" + "="*70)
    print("TEST 1: Module Imports")
    print("="*70)

    try:
        from core import GalacticBrain
        print("✓ core.GalacticBrain")

        from core.ai_modules import QuantumAI, LebensblumeAI, UrspiritAI
        print("✓ core.ai_modules (3 AI systems)")

        from core.agents import SocialAgent, FinanceAgent, CreatorAgent
        print("✓ core.agents (3 agents)")

        from app.database.db import init_db, get_db, save_message, get_history, clear_history
        print("✓ app.database.db (5 functions)")

        return True
    except Exception as e:
        print(f"❌ Import Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_core_initialization():
    """Test 2: Core Module Initialization"""
    print("\n" + "="*70)
    print("TEST 2: Core Module Initialization")
    print("="*70)

    try:
        from core import GalacticBrain

        brain = GalacticBrain()
        print("✓ GalacticBrain created")

        assert brain.quantum_ai is not None
        print("✓ QuantumAI module loaded")

        assert brain.lebensblume_ai is not None
        print("✓ LebensblumeAI module loaded")

        assert brain.urspirit_ai is not None
        print("✓ UrspiritAI module loaded")

        assert len(brain.agents) == 3
        print("✓ 3 Agents loaded")

        return True
    except Exception as e:
        print(f"❌ Initialization Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_brain_processing():
    """Test 3: Brain Processing"""
    print("\n" + "="*70)
    print("TEST 3: Brain Processing")
    print("="*70)

    try:
        from core import GalacticBrain

        brain = GalacticBrain()

        tests = [
            ("Hallo", "Simple greeting"),
            ("quantum", "Quantum AI"),
            ("blume", "Lebensblume AI"),
            ("spirit", "Urspirit AI"),
            ("geld", "Finance Agent"),
            ("create", "Creator Agent"),
            ("social", "Social Agent"),
        ]

        for msg, description in tests:
            responses = brain.process(msg)
            assert len(responses) > 0
            assert len(responses[0]) > 0
            print(f"✓ {description}: {responses[0][:40]}...")

        return True
    except Exception as e:
        print(f"❌ Processing Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_database():
    """Test 4: Database"""
    print("\n" + "="*70)
    print("TEST 4: Database")
    print("="*70)

    try:
        from app.database.db import init_db, get_db

        init_db()
        print("✓ Database initialized")

        conn = get_db()
        assert conn is not None
        print("✓ Database connection established")

        conn.close()
        print("✓ Database connection closed")

        return True
    except Exception as e:
        print(f"❌ Database Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_flask_app():
    """Test 5: Flask App"""
    print("\n" + "="*70)
    print("TEST 5: Flask App & Routes")
    print("="*70)

    try:
        from main import app
        print("✓ main.py imported")

        with app.test_client() as client:
            # Test Homepage
            response = client.get('/')
            assert response.status_code == 200
            print(f"✓ GET / : {response.status_code}")

            # Test API Status
            response = client.get('/api/status')
            assert response.status_code == 200
            data = response.get_json()
            print(f"✓ GET /api/status : {response.status_code}")
            print(f"  - Status: {data.get('status')}")
            print(f"  - Version: {data.get('version')}")
            print(f"  - Modules: {len(data.get('modules', []))} loaded")

            # Test Chat
            response = client.post('/chat',
                json={'message': 'test'},
                headers={'Content-Type': 'application/json'})
            assert response.status_code == 200
            data = response.get_json()
            print(f"✓ POST /chat : {response.status_code}")
            print(f"  - Response: {data.get('response')[:40]}...")

        return True
    except Exception as e:
        print(f"❌ Flask Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("""
╔════════════════════════════════════════════════════════════════════════╗
║                                                                        ║
║      🌌 GALACTIC SINGULARITY ULTRA 2.0 - INTEGRATION TEST 🌌          ║
║                                                                        ║
║              Neue Modularisierte Struktur                            ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
    """)

    results = {
        "Imports": test_imports(),
        "Core Init": test_core_initialization(),
        "Brain Process": test_brain_processing(),
        "Database": test_database(),
        "Flask App": test_flask_app(),
    }

    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test_name, result in results.items():
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")

    print(f"\n📊 Result: {passed}/{total} tests passed")

    if passed == total:
        print("\n" + "="*70)
        print("✨ ALL TESTS PASSED! ✨")
        print("="*70)
        print("\n🚀 APP IS READY TO LAUNCH!\n")
        print("Start with:")
        print("  python3 launcher.py")
        print("  or")
        print("  python3 main.py")
        print("\nThen open: http://localhost:5000\n")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed!\n")
        return 1


if __name__ == '__main__':
    sys.exit(main())

